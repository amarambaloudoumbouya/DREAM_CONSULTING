from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import TemoignageAdminForm, TemoignagePublicForm
from .models import Temoignage


def donner_avis(request):
    form = TemoignagePublicForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            temoignage = form.save(commit=False)
            temoignage.statut = 'en_attente'
            temoignage.save()
            messages.success(
                request,
                "Merci pour votre avis ! Il sera publié après validation par notre équipe.",
            )
            return redirect('site_:donner_avis')
        messages.error(request, 'Veuillez corriger les erreurs du formulaire.')

    return render(request, 'pages/donner_avis.html', {'form': form})


@login_required
def admin_temoignage_list(request):
    statut = request.GET.get('statut')
    temoignages = Temoignage.objects.all()
    if statut:
        temoignages = temoignages.filter(statut=statut)

    total = Temoignage.objects.count()
    total_attente = Temoignage.objects.filter(statut='en_attente').count()
    total_publies = Temoignage.objects.filter(statut='publie').count()
    total_refuses = Temoignage.objects.filter(statut='refuse').count()

    def pct(value):
        if not total:
            return 0
        return round((value / total) * 100)

    return render(request, 'backend/temoignage/index.html', {
        'temoignages': temoignages,
        'total': total,
        'total_attente': total_attente,
        'total_publies': total_publies,
        'total_refuses': total_refuses,
        'pct_attente': pct(total_attente),
        'pct_publies': pct(total_publies),
        'pct_refuses': pct(total_refuses),
        'selected_statut': statut,
        'statut_choices': Temoignage.STATUT_CHOICES,
        'edit_forms': {
            t.pk: TemoignageAdminForm(instance=t, prefix=f'edit-{t.pk}')
            for t in temoignages
        },
    })


@login_required
def admin_temoignage_update(request, pk):
    temoignage = get_object_or_404(Temoignage, pk=pk)

    if request.method != 'POST':
        return redirect('temoignage:admin_list')

    form = TemoignageAdminForm(
        request.POST,
        request.FILES,
        instance=temoignage,
        prefix=f'edit-{pk}',
    )
    if form.is_valid():
        obj = form.save(commit=False)
        if obj.statut == 'publie' and not obj.publie_at:
            obj.publie_at = timezone.now()
        elif obj.statut != 'publie':
            obj.publie_at = None
        obj.save()
        messages.success(request, 'Témoignage mis à jour.')
    else:
        messages.error(request, 'Erreur lors de la modification du témoignage.')

    return redirect('temoignage:admin_list')


@login_required
def admin_temoignage_publier(request, pk):
    if request.method == 'POST':
        temoignage = get_object_or_404(Temoignage, pk=pk)
        temoignage.publier()
        messages.success(request, f'Témoignage de {temoignage.full_name} publié.')
    return redirect('temoignage:admin_list')


@login_required
def admin_temoignage_refuser(request, pk):
    if request.method == 'POST':
        temoignage = get_object_or_404(Temoignage, pk=pk)
        temoignage.refuser()
        messages.success(request, f'Témoignage de {temoignage.full_name} refusé.')
    return redirect('temoignage:admin_list')


@login_required
def admin_temoignage_delete(request, pk):
    if request.method == 'POST':
        temoignage = get_object_or_404(Temoignage, pk=pk)
        temoignage.delete()
        messages.success(request, 'Témoignage supprimé.')
    return redirect('temoignage:admin_list')
