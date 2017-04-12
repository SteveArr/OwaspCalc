from django.db import models
from django.core.urlresolvers import reverse

class RiskItemDetail(models.Model):
    RISK_CATEGORIES = (
        ('SKILL-LEVEL', 'Skill level'),
        ('MOTIVATION', 'Motivation'),
        ('OPPORTUNITY','Opportunity'),
        ('SIZE', 'Size'),
        ('EASE-OF-DISCOVERY', 'Ease of discovery'),
        ('EASE-OF-EXPLOIT', 'Ease of exploit'),
        ('AWARENESS', 'Awareness'),
        ('INTRUSION-DETECTION', 'Intrusion detection'),
        ('LOSS-OF-CONFIDENTIALTY', 'Loss of confidentiality'),
        ('LOSS-OF-INTEGRITY', 'Loss of integrity'),
        ('LOSS-OF-AVAILABILITY', 'Loss of availability'),
        ('LOSS-OF-ACCOUNTABILITY', 'Loss of accountability'),
        ('FINANCIAL-DAMAGE', 'Financial damage'),
        ('REPUTATION-DAMAGE', 'Reputation damage'),
        ('NON-COMPLIANCE', 'Non-compliance'),
        ('PRIVACY-VIOLATION', 'Privacy violation'),
    )
    title = models.CharField(max_length=256)
    score = models.IntegerField(choices=[(i,i) for i in range(1,10)])
    cat = models.CharField(max_length=25, choices=RISK_CATEGORIES)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "[" + str(self.score) + "] " + self.title

class RiskAudit(models.Model):
    title = models.CharField(max_length=256)
    details = models.TextField()
    created_time_stamp = models.DateTimeField(auto_now=True)
    slug = models.SlugField(db_index=True, unique=True)
    skill_level = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'SKILL-LEVEL'},
        related_name='+'
    )
    motivation = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'MOTIVATION'},
        related_name='+',
    )
    opportunity = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'OPPORTUNITY'},
        related_name='+',
    )
    size = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'SIZE'},
        related_name='+',
    )
    ease_of_discovery = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'EASE-OF-DISCOVERY'},
        related_name='+',
    )
    ease_of_exploit = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'EASE-OF-EXPLOIT'},
        related_name='+',
    )
    awareness = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'AWARENESS'},
        related_name='+',
    )
    intrusion_detection = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'INTRUSION-DETECTION'},
        related_name='+',
    )
    loss_of_confidentiality = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'LOSS-OF-CONFIDENTIALTY'},
        related_name='+',
    )
    loss_of_integrity = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'LOSS-OF-INTEGRITY'},
        related_name='+',
    )
    loss_of_availability = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'LOSS-OF-AVAILABILITY'},
        related_name='+',
    )
    loss_of_accountability = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'LOSS-OF-ACCOUNTABILITY'},
        related_name='+',
    )
    financial_damage = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'FINANCIAL-DAMAGE'},
        related_name='+',
    )
    reputation_damage = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'REPUTATION-DAMAGE'},
        related_name='+',
    )
    non_compliance = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'NON-COMPLIANCE'},
        related_name='+',
    )
    privacy_violation = models.ForeignKey(
        RiskItemDetail,
        limit_choices_to={'cat':'PRIVACY-VIOLATION'},
        related_name='+',
    )
        
    class Meta:
        ordering = ["-created_time_stamp"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_slug', kwargs={'slug': self.slug})
    

