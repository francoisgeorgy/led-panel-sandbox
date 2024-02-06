
void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = (fragCoord * 2.0 - iResolution.xy) / iResolution.y;
    float d = length(uv);
    d -= 0.5;
    d = abs(d);
    fragColor = vec4(d, d, d, 1.);
}
