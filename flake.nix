{
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-25.11";
    systems.url = "github:nix-systems/default";
  };

  outputs =
    { nixpkgs, systems, ... }:

    let
      config.packageOverrides = pkgs: {
        udpipe = pkgs.callPackage ./nix/packages/udpipe.nix { };
        pepper = pkgs.callPackage ./nix/packages/pepper.nix { };
      };

      eachSystem =
        f: nixpkgs.lib.genAttrs (import systems) (system: (f (import nixpkgs { inherit system config; })));
    in

    {
      devShells = eachSystem (pkgs: {
        default = pkgs.mkShell {
          packages = with pkgs; [
            (python3.withPackages (
              ps: with ps; [
                pandas
                openpyxl
              ]
            ))
            wget
            w3m
            udpipe
            pepper
          ];

          shellHook = ''
            rm -f udpipe pepper
            ln -s ${pkgs.udpipe}/bin/udpipe udpipe
            ln -s ${pkgs.pepper}/share/pepper pepper
          '';
        };
      });
    };
}
