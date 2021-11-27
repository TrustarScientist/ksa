from django.db import models

# Create your models here.
class Niche(models.Model):
    name = models.CharField(max_length=50)
    

class NicheMeta(models.Model):
    niche = models.ForeignKey(Niche, on_delete=models.CASCADE)
    parent = models.ForeginKey(Niche, on_delete=models.CASCADE)

class NicheFollower(models.Model):
    niche = models.ForeignKey(Niche, on_delete=models.CASCADE, related_name="follower")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="following")
    started_following = models.DateField(auto_now_add=True)
