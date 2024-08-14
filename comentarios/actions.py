def reprova_comentarios(modelAdmin, request, queryset):
    queryset.update(aprovado=False)


def aprova_comentarios(modelAdmin, request, queryset):
    queryset.update(aprovado=True)

reprova_comentarios.short_descriptions = 'Reprova comentarios'
aprova_comentarios.short_descriptions = 'Aprova comentarios'