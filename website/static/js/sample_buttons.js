let SampleTitleButton = document.getElementById('sample-title-button');
let Title = document.getElementById('papertitle');
let SampleAbstractButton = document.getElementById('sample-abstract-button');
let Abstract = document.getElementById('paperabstract');

const ThesisTitle = 'On Generalizations of p-Adic Weierstrass Sigma and Zeta Functions';
const ThesisAbstract = 'We generalize a paper of Mazur and Tate on p-adic sigma functions attached to elliptic curves of ordinary reduction over a p-adic field. We begin by generalizing the theory of division polynomials attached to an isogeny of elliptic curves, developed by Mazur and Tate, to isogenies of prinicipally polarized abelian varieties. As an application, we produce a notion of a p-adic sigma function attached to a prinicipally polarized abelian variety of good ordinary reduction over a complete non-archimedean field of residue characteristic p.Furthermore, we derive some the properties of the sigma function, many of which uniquely characterize the function.Independently, a notion of a pair of p-adic Weierstrass zeta functions is produced for a smooth projective curve C of genus two with invertible Hasse--Witt matrix over a p-adically complete field of characteristic zero. Using the explicit function theory afforded by Jacobians of genus two, general results about p-adic sigma functions are made more descriptive and the zeta functions on C are compared to the second logarithmic derivatives of the sigma function on the Jacobian of C.';

SampleTitleButton.onclick = () => {
    Title.value = ThesisTitle;
};

SampleAbstractButton.onclick = () => {
    Abstract.value = ThesisAbstract;
};

