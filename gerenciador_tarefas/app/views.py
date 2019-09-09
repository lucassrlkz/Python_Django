from django.shortcuts import render

# Create your views here.
def listar_tarefas(request):
    nome_tarefa ="passando raiva com o bd mysql"
    return render(request, 'tarefas/listar_tarefas.html',{"nome_tarefa":nome_tarefa})