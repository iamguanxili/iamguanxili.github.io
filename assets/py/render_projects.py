from render_utils import *

def generate_Research_html():
    Research_html = f"""
    <!DOCTYPE HTML>
    <!--
        Verti by HTML5 UP
        html5up.net | @ajlkn
        Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
    -->
    <html>
        {generate_head_html()}
        <body class="is-preload homepage">
            <div id="page-wrapper">

                {generate_header_html("Research")}

                <!-- Main -->
				<div id="main-wrapper">
					<div class="container">
						<div id="content">

							<!-- Content -->
								<article>
									<h2>Undergraduate</h2>
									<h3>2023</h3>
									<p>
										<strong><a href="https://mxgo111.github.io/assets/pdfs/final_senior_thesis.pdf" target="_blank">On Neural Linear Model Prediction</a></strong> (Senior Thesis). <br />
										<strong><a href="https://mxgo111.github.io/assets/pdfs/AM201_Project.pdf" target="_blank">Solving the 3d Heat Equation with the Finite Element Method</a></strong> (Applied Math 201 Final Project).<br />
										<strong><a href="https://mxgo111.github.io/assets/pdfs/Econ980kk_Project.pdf" target="_blank">Solving Schumpeterian Models of Business Process and Product Innovation with Reinforcement Learning</a></strong> (Economics 980kk Final Project). <br />
									</p>

									<h3>2022</h3>
									<p>
										<strong><a href="https://mxgo111.github.io/assets/pdfs/AISG-23_paper_2458_camera_ready.pdf" target="_blank">Using Satellite Imagery to Predict Multidimensional Poverty in Nigeria</a></strong> (Computer Science 288 Final Project, accepted as short paper at AAAI 2023 Workshop on AI for Social Good).<br />
										<!-- <strong>Understanding Deep Bayesian Methods</strong> (<a href="https://dtak.github.io/" target="_blank">DtAK Lab</a> Research Project, Ongoing. <a href="https://mxgo111.github.io/assets/pdfs/spuds_slides.pdf" target="_blank">SPUDS talk slides</a>).<br /> -->
										<!-- <strong><a href="reviews.html">Reading Papers on AI</a></strong> (Individual Project, Ongoing).<br /> -->
										<strong><a href="https://mxgo111.github.io/assets/pdfs/Stat195_Writeup_Individual.pdf" target="_blank">Feature Sparsity in Protein Sequence Design using LassoNet</strong></a> (Statistics 195 Final Project).<br />
										<strong><a href="https://mxgo111.github.io/assets/pdfs/CS238_Project.pdf" target="_blank">An Epistemic Approach in Multiple Social Issues</a></strong> (Computer Science 238 Final Project).<br />

									</p>
									
									<h3>2021</h3>
									<p>
										<strong><a href="https://github.com/mxgo111/Object-Detector-Pipeline" target="_blank">Object Detector for Lab Equipment</a></strong> (<a href="https://lit.gse.harvard.edu/" target="_blank">LIT Lab</a> Research Project).<br />
										<strong><a href="https://mxgo111.github.io/assets/pdfs/AM207_Group_Project.pdf" target="_blank">Measuring Data Leakage using Fisher Information Loss</strong></a> (Applied Math 207 Final Project).<br />
										<strong><a href="https://mxgo111.github.io/assets/pdfs/Stat185_Paper.pdf" target="_blank">An Analysis of t-SNE</a></strong> (Statistics 185 Final Project).<br />
										<strong><a href="https://mxgo111.github.io/assets/pdfs/CS282br_Project.pdf" target="_blank">Regret Minimization in Gambler Bandits</a></strong> (Computer Science 282br Final Project).<br />
										<strong><a href="https://mxgo111.github.io/assets/pdfs/Sleep_Midterm.pdf" target="_blank">Data Analysis on Sleep Time and Quality</a></strong> (General Education 1038 Project).<br />
										<strong><a href="https://mxgo111.github.io/assets/pdfs/CS234r_Literature_Review.pdf" target="_blank">Influence and Revenue Maximization in Social Networks</a></strong> (Computer Science 234r Final Project).<br />
										<strong><a href="https://mxgo111.github.io/assets/pdfs/CS181_Practical.pdf" target="_blank">Machine Learning for Sound Classification</a></strong> (Computer Science 181 Practical).<br />
									</p>

									<h3>2020</h3>
									<p>
										<strong><a href="https://mxgo111.github.io/assets/pdfs/CS182_Final_Paper.pdf" target="_blank">Machine Learning to Predict Academic Achievement</a></strong> (Computer Science 182 Final Project).<br />
										<strong><a href="https://mxgo111.github.io/assets/pdfs/AM205_Final_Paper.pdf" target="_blank">Numerical Image Inpainting Methods</a></strong> (Applied Math 205 Final Project).<br />
										<strong>Deep Learning for Image Reconstruction</strong> (<a href="https://crisp.seas.harvard.edu/" target="_blank">CRISP Group</a> Research Project).<br />
										<strong><a href="https://github.com/RashedRifat/Multiple-Object-Style-Transfer" target="_blank">Selective Stylization using Detectron2 and Neural Style Transfer</a></strong> (<a href="https://madewithml.com/" target="_blank">Made With ML Incubator</a> Project). <br />
									</p>

									<h3>2019</h3>
									<p>
										<strong><a href="https://mxgo111.github.io/assets/pdfs/MIT_Primes_Paper.pdf" target="_blank">Behavior of Bar-Natan Homology under Conway Mutation</a></strong> (MIT PRIMES Research Project). <br />
									</p>
								</article>

						</div>
					</div>
				</div>

                {generate_footer_html()}

                {generate_scripts_html()}

        </body>
    </html>
    """

    return Research_html