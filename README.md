# Turbo Code Interactive Simulator 📡

## 📝 Présentation

Ce projet est une plateforme éducative interactive permettant de simuler et de visualiser les performances des **Turbo Codes**, une classe de codes correcteurs d'erreurs hautes performances utilisés dans les standards de télécommunications modernes (4G, communications satellites).

L'application démontre le cycle de vie complet d'une transmission numérique : de la génération des données sources au décodage itératif, en passant par la modulation QPSK et la traversée d'un canal bruité (AWGN).

## 🚀 Fonctionnalités Clés

* **Chaîne de transmission complète** : Intégration de l'encodage convolutif parallèle, de l'entrelacement et de la modulation QPSK.
* **Simulation de Canal Réaliste** : Modélisation d'un canal à Bruit Blanc Additif Gaussien (AWGN).
* **Interface Interactive (IPython Widgets)** : Ajustement en temps réel du rapport Signal/Bruit (SNR) et du nombre d'itérations de décodage.
* **Visualisation Avancée** :
* Diagramme de constellation QPSK.
* Courbe de convergence du décodeur itératif.
* Comparaison temporelle des bits (Source vs Décodés) avec calcul du Taux d'Erreur Binaire (BER).



## 🛠️ Installation

1. **Cloner le dépôt** :

A venir


2. **Installer les dépendances** :
```bash
pip install numpy matplotlib ipywidgets

```


3. **Lancer le simulateur** :
Ouvrez le fichier `Turbo_code_interactif.ipynb` ou lancez le script Python dans un environnement supportant les widgets (Jupyter Notebook, Lab ou VS Code).

## 📖 Architecture du Code

Le projet est segmenté en modules logiques reflétant les étapes de traitement du signal :

* **`generate_bits()`** : Génération de la séquence binaire aléatoire.
* **`turbo_encoder()`** : Implémentation du codage concaténé parallèle avec entrelaceur.
* **`qpsk_mod()`** : Transformation des bits en symboles complexes sur le plan I/Q.
* **`awgn()`** : Injection de bruit thermique paramétrable.
* **`turbo_decode_soft()`** : Algorithme de décodage itératif simulant l'échange d'informations extrinsèques.

## 📊 Analyse des Performances

Le simulateur permet d'observer deux phénomènes fondamentaux :

1. **L'effet de seuil** : En dessous d'un certain SNR, le décodage échoue brutalement.
2. **Le gain d'itération** : À SNR constant, l'augmentation du nombre d'itérations réduit significativement le BER, illustrant la convergence du décodeur.

## 📄 Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

---