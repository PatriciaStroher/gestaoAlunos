from django.db import models

# Create your models here.

class AlunoNovo(models.Model):
 Nome = models.CharField(max_length=100, verbose_name=u'Nome')
 Endereco = models.CharField(max_length=100)
 Idade =  models.CharField(max_length=100)
 Serie =  models.CharField(max_length=100)
 Pagamento = models.DateTimeField()

 def __str__(self):
 	return self.Nome


class Horario(models.Model):
 alunoNovo = models.foreignkey(AlunoNovo) 
 NomeAluno = models.CharField(max_length=100, verbose_name=u'Nome Aluno')
 DiasDaSemana = models.CharField(max_length=50)
 horaDasAulas = models.CharField(max_length=40)
 

 def __str__(self):
		return self.NomeAluno
