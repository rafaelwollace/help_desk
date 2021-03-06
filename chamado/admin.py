
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from chamado.models import Chamado, RespostaChamado
from tipo_chamado.models import Sistema, TipoChamado

# Register your models here.


class RespostachamadoTabularInline(admin.StackedInline):
    model = RespostaChamado
    readonly_fields = ('resposta_data', 'resposta_autor',)
    extra = 0


class ChamadoAdmin(admin.ModelAdmin):
    inlines = [RespostachamadoTabularInline]
    model = Chamado
    list_display = ['id', 'data_chamado', 'status_chamado',
                    'hora_chamado', 'arquivo_chamado', 'sistema', 'tipochamado', 'tecnico_chamado']
    list_filter = ('usuario', 'tecnico_chamado',)
    readonly_fields = ('usuario', 'tecnico_chamado',
                       'status_chamado', 'show_firm_url',)
    list_editable = ('tecnico_chamado',)

    @mark_safe
    def show_firm_url(self, ob):
        url = reverse('admin:users_user_change', args=(ob.usuario_id, ))
        return '<a class="related-widget-wrapper-link add-related"  href="{url}" >Veja aqui</a>'.format(
            url=url
        )

    show_firm_url.short_description = "Inf. do Usúario."

    # TODO: SETAR USUARIO LOGADO NO MODELADM

    def save_model(self, request, obj, form, change):
        if obj.usuario is None:
            obj.usuario = request.user
            obj.save()
        else:
            obj.tecnico_chamado
        obj.save()

        # TODO: SETA USUARIO LOGADO NO INLINE
    def save_formset(self, request, form, formset, change):
        for inline_form in formset.forms:
            if inline_form.has_changed():
                inline_form.instance.resposta_autor = request.user
        super().save_formset(request, form, formset, change)

    # TODO: DESABILITAR PARA EDIÇÃO
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('arquivo_chamado', 'descricao_chamado', 'sistema', 'tipochamado',)
        return self.readonly_fields

    # TODO: VISUALIZAR APENAS O QUE É SEU
    def get_queryset(self, request):
        qs = super(ChamadoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)


# Register your models here.
admin.site.register(Chamado, ChamadoAdmin)
