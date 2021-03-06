# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Algorithms (:mod:`qiskit.algorithms`)
==========================================
It contains a collection of quantum algorithms, for use with quantum computers, to
carry out research and investigate how to solve problems in different domains on
near-term quantum devices with short depth circuits.

Algorithms configuration includes the use of :mod:`~qiskit.algorithms.optimizers`
and :mod:`~qiskit.algorithms.variational_forms` which
were designed to be swappable sub-parts of an algorithm. Any component and may be exchanged for
a different implementation of the same component type in order to potentially alter the behavior
and outcome of the algorithm.

Quantum algorithms are run via a :class:`~qiskit.algorithms.QuantumInstance`
which must be set with the
desired backend where the algorithm's circuits will be executed and be configured with a number of
compile and runtime parameters controlling circuit compilation and execution. It ultimately uses
`Terra <https://www.qiskit.org/terra>`__ for the actual compilation and execution of the quantum
circuits created by the algorithm and its components.

.. currentmodule:: qiskit.algorithms

Algorithms Base Class
=====================

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   QuantumAlgorithm

Algorithms
==========

It contains a variety of quantum algorithms and these have been grouped by logical function such
as minimum eigensolvers and amplitude amplifiers.

Amplitude Amplifiers
++++++++++++++++++++

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   Grover
   GroverResult

Eigensolvers
++++++++++++
Algorithms to find eigenvalues of an operator. For chemistry these can be used to find excited
states of a molecule and qiskit.chemistry has some algorithms that leverage chemistry specific
knowledge to do this in that application domain.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   Eigensolver
   EigensolverResult

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   NumPyEigensolver

Factorizers
+++++++++++
Algorithms to find factors of a number.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   Shor

Minimum Eigensolvers
++++++++++++++++++++
Algorithms that can find the minimum eigenvalue of an operator.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   MinimumEigensolver
   MinimumEigensolverResult

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   NumPyMinimumEigensolver
   QAOA
   VQE

Exceptions
==========

.. autosummary::
   :toctree: ../stubs/

   AlgorithmnError
"""

from .algorithm_result import AlgorithmResult
from .quantum_algorithm import QuantumAlgorithm
from .variational_quantum_algorithm import VQAlgorithm, VQResult
from .amplitude_amplifiers import Grover, GroverResult
from .eigen_solvers import NumPyEigensolver, ExactEigensolver, Eigensolver, EigensolverResult
from .factorizers import Shor
from .minimum_eigen_solvers import (VQE, VQEResult, QAOA,
                                    NumPyMinimumEigensolver,
                                    MinimumEigensolver, MinimumEigensolverResult)
from .exceptions import AlgorithmError

__all__ = [
    'AlgorithmResult',
    'QuantumAlgorithm',
    'VQAlgorithm',
    'VQResult',
    'Grover',
    'GroverResult',
    'NumPyEigensolver',
    'ExactEigensolver',
    'Eigensolver',
    'EigensolverResult',
    'Shor',
    'VQE',
    'VQEResult',
    'QAOA',
    'NumPyMinimumEigensolver',
    'MinimumEigensolver',
    'MinimumEigensolverResult',
    'AlgorithmError',
]
