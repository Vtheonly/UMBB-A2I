```tikz
\documentclass{standalone}
\usepackage{tikz}

\begin{document}

% Diagram 1: Fully Connected Neural Network
\begin{tikzpicture}[x=1.5cm, y=1.5cm]
    \tikzstyle{neuron}=[circle,fill=white,draw,minimum size=1cm]
    \tikzstyle{input neuron}=[neuron, fill=white];
    \tikzstyle{output neuron}=[neuron, fill=white];
    \tikzstyle{hidden neuron}=[neuron, fill=white];
    \tikzstyle{annot} = [text width=4em, text centered]

    % Draw the input layer nodes
    \foreach \name / \y in {1,...,5}
        \node[input neuron] (I-\y) at (0,-\y) {};

    % Draw the hidden layer nodes
    \foreach \name / \y in {1,...,4}
        \node[hidden neuron] (H-\y) at (3,-1.25-\y*0.5) {};

    % Draw the output layer node
    \node[output neuron] (O) at (6,-3) {};

    % Connect every input node to every hidden node
    \foreach \source in {1,...,5}
        \foreach \dest in {1,...,4}
            \path[->] (I-\source) edge (H-\dest);

    % Connect every hidden node to the output node
    \foreach \source in {1,...,4}
        \path[->] (H-\source) edge (O);

    % Draw the input arrows
    \foreach \y in {1,...,5}
        \draw[->] (-1, -\y) -- (I-\y) node[pos=0, left] {Input \y};

    % Draw the output arrow
    \draw[->] (O) -- (7,-3) node[right] {Output};

    % Add layer labels
    \node[annot,above of=I-1, node distance=1cm] (il) {Input layer};
    \node[annot,above of=H-1, node distance=1cm] {Hidden layer};
    \node[annot,above of=O, node distance=1cm] {Output layer};
\end{tikzpicture}

\vspace{2cm} % Add some vertical space between the two diagrams

% Diagram 2: Single Neuron Computation
\begin{tikzpicture}[x=1.5cm, y=1.5cm]
    % Inputs and weights
    \foreach \i in {1,2,3}
        \node (x\i) at (0, 1.5-\i) {$x_\i$};

    \draw (0.5, 1.5-1) -- (1.5, 1.5-1) node[pos=0.5, above] {$w_1$};
    \draw (0.5, 1.5-2) -- (1.5, 1.5-2) node[pos=0.5, above] {$w_2$};
    \draw (0.5, 1.5-3) -- (1.5, 1.5-3) node[pos=0.5, above] {$w_3$};

    \foreach \i in {1,2,3}
        \draw[o->] (x\i) -- (0.5, 1.5-\i);

    % Summation node
    \node[circle, draw, inner sep=0.1cm] (sum) at (2.5, 0) {$\sum$};
    \foreach \i in {1,2,3}
        \draw[->] (1.5, 1.5-\i) -- (sum);
        
    % Bias
    \node (b) at (2.5, 1.5) {$b$};
    \draw[o->] (b) -- (sum);
    \node[above of=b, node distance=0.4cm] {Bias};

    % Activation function
    \node[draw, minimum width=0.7cm, minimum height=0.7cm] (act) at (4, 0) {$f$};
    \draw[->] (sum) -- (act);
    \node[above of=act, node distance=0.6cm, text width=2cm, align=center] {Activate function};
    
    % Output
    \node (y) at (5.5, 0) {$y$};
    \draw[->] (act) -- (y);
    \node[right of=y, node distance=1cm] {};
    \node[above of=y, node distance=0.4cm] {Output};
    
    % Labels for inputs and weights
    \draw [decorate,decoration={brace,amplitude=10pt}] (-0.5,1.1) -- (-0.5,-1.1) node [black,midway,xshift=-0.6cm] {Inputs};
    \node at (1, -1.5) {Weights};
\end{tikzpicture}

\end{document}