#define S .4

void mainImage( out vec4 U, in vec2 V )
{
    vec2 u = V * 2. / iResolution.y;

    U = vec4( step( abs( mod( u - iTime * S, S ) - S * .5 ).x + abs( mod( u, S ) - S * .5 ).y - S * .5, 0. ) );
}