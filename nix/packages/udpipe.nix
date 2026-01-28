{
  stdenv,
  fetchFromGitHub,
}:

stdenv.mkDerivation rec {
  name = "udpipe";
  version = "1.4.0";

  src = fetchFromGitHub {
    owner = "ufal";
    repo = name;
    tag = "v${version}";
    hash = "sha256-ekRuaQlNGv+7eFtwqbs6d6hy/b8uZpHq2ffcKPcre7U=";
  };

  preBuild = ''
    cd src
  '';

  installPhase = ''
    mkdir -p $out/bin
    cp udpipe $out/bin/
  '';
}
