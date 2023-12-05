# Infection-Tracing
Project for Machine Learning on Real World Networks

## Docs
- The `docs` folder contains all of the reports - M0, M1, M2, M3
    - The final report is under the `M3` folder

## 5-Day Contact Network Generation and Static Link Prediction
- The `graph_creation` folder contains code that creates the `5-Day Contact Network` and analyzes it
    - `main.ipynb` creates the contact network
    - `analysis.ipynb` analyzes the contact network
- The `link_prediction` folder contains code for static link prediction as well as node feature generation for the nodes in the `5-Day Contact Network`
    - `feature_selection_method1` contains code to generate `average locations travelled to per day` and `average distance travelled per day` for each node
    - `feature_selection_method2` contains code to extract `age`, `gender`, and `SAG score` for each node
    - `feature_combination` contains code that combines all features and normalizes them
    - `main.ipynb` contains the code to train the static link prediction model on the 5-Day Contact Network
    - `link_prediction_next_day.ipynb` contains the code to perform link prediction on the 6th day using the static link prediction model

## Temporal Contact Networks Generation and Temporal Link Prediction
- The `link_prediction_graph_creation` folder contains code that creates the `Temporal Contact Networks`, performs analysis on those networks, generates node features for nodes in the `Temporal Contact Networks`, formats the 62 contact networks to be able to be used by the TGN model, and performs an SIR simulation on the `Temporal Contact Networks`
    - `main.py` creates the 62 contact networks, one for each day from July 1st, 2020 to August 31st, 2020.
    - `feature_selection_method1` contains code to generate `average locations travelled to per day` and `average distance travelled per day` for each node
    - `feature_selection_method2` contains code to extract `age`, `gender`, and `SAG score` for each node
    - `feature_combination` contains code that combines all features and normalizes them
    - `generate_link_pred_input.ipynb` contains code that utilizes the Temporal Contact Networks and their features to generate a data format that can be used by the TGN link prediction framework (convert `.gexf` files to `csv` and `npy` files)
    - `simulation.py` contains code that uses the `Temporal Contact Networks` to run an SIR simulation

### TGN Framework
- The `tgn` folder contains the code (which is open source and created by the authors or TGN) that is used for the temporal link prediction
    - Original TGN GitHub: `https://github.com/twitter-research/tgn`
    - Original TGN Paper: `https://arxiv.org/abs/2006.10637`
    - `data` contains data used by the framework, which includes edge data and node data
    - `evaluation` contains code what evaluates the model. We modified this to plot the ROC AUC curve and generate the confusion matrix that can be used to determine recall
    - `modules` contains code for the main modules in the TGN framework
        - `memory.py` - stores memory for the nodes
        - `message_function.py` - generates messages (information) regarding each node interaction (such as creation of edges)
        - `message_aggregator.py` - combines a batch of messages to keep one per node
        - `memory_updater.py` - updates the memory using the current memory and new messages
        - `embedding_module.py` - generates node embeddings by using the node interaction (such as creation of edges) and the node memory
    - `model` contains code for the model that is used by the embedding module to create node embeddings
    - `train_self_supervised.py` contains the code to train and test the temporal link prediction model
    - `generate_visuals.ipynb` contains the code to generate charts and graphs such as ROC Curve and Precision-Recall Curve to visualize the results