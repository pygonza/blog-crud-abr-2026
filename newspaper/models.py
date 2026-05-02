from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, help_text="Título atractivo y descriptivo del artículo")
    content = models.TextField(help_text="Contenido completo del artículo")
    excerpt = models.TextField(blank=True, help_text="Resumen breve (opcional, se genera automáticamente si está vacío)")
    author = models.ForeignKey('auth.User',
                               on_delete=models.CASCADE
                               )
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

    def get_excerpt(self):
        """Retorna el excerpt o genera uno automáticamente del contenido"""
        if self.excerpt:
            return self.excerpt
        # Genera excerpt automático: primeras 150 caracteres
        return self.content[:150] + '...' if len(self.content) > 150 else self.content

    def save(self, *args, **kwargs):
        # Si no hay excerpt, genera uno automáticamente
        if not self.excerpt and self.content:
            self.excerpt = self.get_excerpt()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"