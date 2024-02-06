
void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = fragCoord / iResolution.xy * 2.0 - 1.0;
    fragColor = vec4(uv.x, uv.y, 0., 1.);
}