Danika Duval a utilisée les modèles d'IA GPT-5.6 Sol Quick response et GPT-5.6 Sol Think deeper sur Microsoft Copilot, version 156.0.4314.50. Les deux modèles ont été utilisés en mode "automatique" par Copilot, selon les consignes fournies. Son objectif d'utilisation était d'augmenter sa compréhension sur les différences entre les licences Apache et MIT

Antoine Reid a utilisé le modèle d'IA DeepSeek-V4.1-Flash-1017 avec l'agent de codage Pi 1.4.0. Il a notamment été utilisé pour
écrire le script permettant le téléchargement des données du répertoire de Borealis. Le prompt spécifique était :
>*Create a script that retrieves the dataset from Borealis. This step ensures that data acquisition is automated and reproducible, rather than performed manually.*

L'auteur a aussi demandé à l'agent de compresser le code et d'utiliser le module `requests`:
>*compress and use requests instead*

Toutefois, l'agent n'a pas compris la directive de compresser le code du premier coup et nous avons dû spécifier qu'il était question du code qui était trop complexe.
