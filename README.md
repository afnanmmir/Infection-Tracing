# Infection-Tracing
Project for Machine Learning on Real World Networks

# Code Explanation
- The `docs` folder contains all of the reports - M0, M1, M2, M3
- The `graph_creation` folder contains code that creates the `5-Day Contact Network` and analyzes it
- The `link_prediction` folder contains code for static link prediction as well as node feature generation
- The `link_prediction_graph_creation` folder contains code that creates the `Temporal Contact Networks`, performs analysis on those networks, generates node features, formats the 62 contact networks to be able to be used by the TGN model
- The `simulation` folder contains code that uses the `Temporal Contact Networks` to run a SIR simulation
- The `tgn` folder contains the code (which is open source and created by the authors or TGN) that is used for the temporal link prediction