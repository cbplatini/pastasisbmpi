from django.db import models


class Estado(models.Model):
	nome = models.CharField(max_length=30)
	obs = models.TextField(blank=True)
	def __str__(self):
		return self.nome

class Cidade_Quartel(models.Model):
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
	nome = models.CharField(max_length=30)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Cidades onde existe quartel"
		
	def __str__(self):
		return self.nome

class Cidade_Natal(models.Model):
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
	nome = models.CharField(max_length=30)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Cidades onde residem militar(es)"
	def __str__(self):
		return self.nome

class Quartel(models.Model):
	cidade = models.ForeignKey(Cidade_Quartel, on_delete=models.CASCADE)
	nome = models.CharField(max_length=30)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Quarteis"
	def __str__(self):
		return self.nome

class Tipo_Patente(models.Model):
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Tipos de patente"
	def __str__(self):
		return self.nome

class Patente(models.Model):
	tipo = models.ForeignKey(Tipo_Patente, on_delete=models.CASCADE)
	nome = models.CharField(max_length=100)
	sigla = models.CharField(max_length=10)
	nivel =models.PositiveSmallIntegerField()
	obs = models.TextField(blank=True)
	class Meta:		
		ordering = ['nivel']
	def __str__(self):
		return self.nome

class Secao(models.Model):
	nome = models.CharField(max_length = 100)
	descricao = models.TextField(blank=True)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Seções"
	def __str__(self):
		return self.nome

class Cargo_Funcao(models.Model):
	tipo = models.CharField(max_length = 100)
	nome = models.CharField(max_length = 100)
	secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
	descricao = models.TextField(blank=True)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Cargos/funções"
	def __str__(self):
		return self.nome

class Comportamento(models.Model):
	nome = models.CharField(max_length=50)
	obs = models.TextField(blank=True)
	def __str__(self):
		return self.nome

class Militar(models.Model):	
	nome = models.CharField(max_length = 100)
	nome_guerra = models.CharField(max_length = 50)
	matricula = models.CharField(max_length = 50)
	email = models.EmailField()
	patente = models.ForeignKey(Patente, on_delete=models.CASCADE)
	lotacao = models.ForeignKey(Quartel, on_delete=models.CASCADE)
	cargo_funcao = models.ForeignKey(Cargo_Funcao, on_delete=models.CASCADE)
	comportamento = models.ForeignKey(Comportamento, on_delete=models.CASCADE)
	data_inclusao = models.DateField()
	sangue = models.CharField(max_length=10)
	data_nascimento = models.DateField()
	grau_instrucao = models.CharField(max_length=100)
	sexo = models.CharField(max_length=30)
	naturalidade = models.ForeignKey(Cidade_Natal, on_delete=models.CASCADE)
	nacionalidade = models.CharField(max_length=30)
	pai = models.CharField(max_length=100)
	mae = models.CharField(max_length=100)
	foto = models.ImageField(upload_to='militares_photo', null=True,blank=True)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Militares"
		ordering = ['patente']
	def __str__(self):             
		return str(self.nome_guerra) + " - " + str(self.patente)

class Promocao(models.Model):
	militar = models.ForeignKey(Militar, on_delete=models.CASCADE)	
	patente_nova = models.ForeignKey(Patente, on_delete=models.CASCADE)
	data = models.DateField()
	documento = models.FileField(blank=True)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Promoções"
		ordering = ['data']

class Tipo_Dispensa(models.Model):
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Tipos de dispensa"
	def __str__(self):
		return self.nome	

class Dispensa(models.Model):
	tipo = models.ForeignKey(Tipo_Dispensa, on_delete=models.CASCADE)
	militar = models.ForeignKey(Militar, on_delete=models.CASCADE)
	descricao = models.CharField(max_length=500, blank=True)
	data_parte = models.DateField()
	data_inicio = models.DateField()
	data_termino = models.DateField()
	documento = models.FileField(blank=True)
	obs = models.TextField(blank=True)
	class Meta:		
		ordering = ['data_parte']
	def __str__(self):             
		return str(self.tipo) + " - " + str(self.militar)

class Ferias(models.Model):
	ano = models.PositiveSmallIntegerField()
	militar = models.ForeignKey(Militar, on_delete=models.CASCADE)
	data_inicio = models.DateField()
	data_termino = models.DateField()
	documento = models.FileField(blank=True)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Férias"
		ordering = ['data_inicio']
	def __str__(self):             
		return str(self.militar) + " - " + str(self.ano)

class Tipo_Recompensa(models.Model):
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Tipos de recompensa"
	def __str__(self):
		return self.nome	

class Recompensa(models.Model):
	tipo = models.ForeignKey(Tipo_Recompensa, on_delete=models.CASCADE)
	militar = models.ForeignKey(Militar, on_delete=models.CASCADE)
	recompensador = models.CharField(max_length=500)
	documento = models.FileField(blank=True)
	obs = models.TextField(blank=True)
	def __str__(self):             
		return str(self.tipo) + " - " + str(self.militar)

class Tipo_Punicao(models.Model):
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Tipos de punição"
	def __str__(self):
		return self.nome	

class Punicao(models.Model):
	tipo = models.ForeignKey(Tipo_Punicao, on_delete=models.CASCADE)
	militar = models.ForeignKey(Militar, on_delete=models.CASCADE)
	data_inicio = models.DateField()
	data_termino = models.DateField()
	dias = models.PositiveSmallIntegerField()
	documento = models.FileField(blank=True)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Punições"
	def __str__(self):             
		return str(self.tipo) + " - " + str(self.militar)		

class Viatura(models.Model):
	especie_tipo = models.CharField(max_length=300)
	combustivel = models.CharField(max_length=50)
	marca_modelo = models.CharField(max_length=300)
	ano_fab = models.PositiveSmallIntegerField()
	ano_mod = models.PositiveSmallIntegerField()
	cor_predominante = models.CharField(max_length=50)
	local = models.ForeignKey(Quartel, on_delete=models.CASCADE)	
	documento = models.FileField(blank=True)
	obs = models.TextField(blank=True)	
	def __str__(self):             
		return self.especie_tipo + " - " + str(self.local)	

class Abastecimento(models.Model):
	viatura = models.ForeignKey(Viatura, on_delete=models.CASCADE)
	odometro = models.CharField(max_length=50)
	combustivel = models.CharField(max_length=50)
	motorista = models.ForeignKey(Militar, on_delete=models.CASCADE)	
	litros = models.DecimalField(max_digits=7, decimal_places=2)
	valor = models.DecimalField(max_digits=7, decimal_places=2)
	data = models.DateField()
	documento = models.FileField(blank=True)
	obs = models.TextField(blank=True)	
	def __str__(self):             
		return str(self.viatura) + " - " + str(self.data)		

class Area_ocorrencia(models.Model):	
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Áreas de ocorrências"
	def __str__(self):
		return self.nome	

class Area_prevencao(models.Model):
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Áreas de prevenção"
	def __str__(self):
		return self.nome			

class Tipo_ocorrencia(models.Model):
	area = models.ForeignKey(Area_ocorrencia, on_delete=models.CASCADE)	
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Tipos de ocorrências"
	def __str__(self):
		return self.nome		

class Tipo_prevencao(models.Model):
	area = models.ForeignKey(Area_prevencao, on_delete=models.CASCADE)	
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Tipos de prevenção"
	def __str__(self):
		return self.nome

class Cidade_ocorrencia(models.Model):
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)	
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Cidades de ocorrências"
	def __str__(self):
		return self.nome		

class Cidade_prevencao(models.Model):
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)	
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Cidades de prevenções"
	def __str__(self):
		return self.nome	

class Bairro_ocorrencia(models.Model):
	cidade = models.ForeignKey(Cidade_ocorrencia, on_delete=models.CASCADE)	
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Bairros de ocorrências"
	def __str__(self):
		return self.nome		

class Bairro_prevencao(models.Model):
	cidade = models.ForeignKey(Cidade_prevencao, on_delete=models.CASCADE)	
	nome = models.CharField(max_length=100)
	obs = models.TextField(blank=True)
	class Meta:
		verbose_name_plural = "Bairros de prevenções"
	def __str__(self):
		return self.nome	

class Ocorrencia(models.Model):
	tipo =  models.ManyToManyField(Tipo_ocorrencia)
	data_saida = models.DateTimeField()
	data_retorno = models.DateTimeField()
	viaturas = models.ManyToManyField(Viatura)
	atendimento = models.ManyToManyField(Quartel)
	bairro = models.ForeignKey(Bairro_ocorrencia, on_delete=models.CASCADE)
	cidade = models.ForeignKey(Cidade_ocorrencia, on_delete=models.CASCADE)
	descricao = models.TextField(max_length=300, blank=True)
	livro = models.CharField(max_length=100)
	obs = models.TextField(max_length=300, blank=True)	
	class Meta:
		verbose_name_plural = "Ocorrências"
		ordering = ['data_saida']

	def get_tipos(self):
		return " / ".join([p.nome for p in self.tipo.all()])

	def get_atendimentos(self):
		return " / ".join([p.nome for p in self.atendimento.all()])
	    	

	def __str__(self):             
		return str(self.tipo) + " - " + str(self.data_saida)	

class Prevencao(models.Model):
	tipo =  models.ManyToManyField(Tipo_prevencao)
	data_saida = models.DateTimeField()
	data_retorno = models.DateTimeField()
	viaturas = models.ManyToManyField(Viatura)
	atendimento = models.ManyToManyField(Quartel)
	bairro = models.ForeignKey(Bairro_prevencao, on_delete=models.CASCADE)
	cidade = models.ForeignKey(Cidade_prevencao, on_delete=models.CASCADE)
	descricao = models.TextField(max_length=300, blank=True)
	livro = models.CharField(max_length=100)
	documento = models.FileField(blank=True)
	obs = models.TextField(max_length=300, blank=True)	
	class Meta:
		verbose_name_plural = "Prevenções"
		ordering = ['data_saida']

	def get_tipos(self):
		return " / ".join([p.nome for p in self.tipo.all()])

	def get_atendimentos(self):
		return " / ".join([p.nome for p in self.atendimento.all()])
	    	

	def __str__(self):             
		return str(self.tipo) + " - " + str(self.data_saida)									