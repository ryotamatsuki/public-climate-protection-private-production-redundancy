import Lake
open Lake DSL

package pcppr where

require mathlib from git "https://github.com/leanprover-community/mathlib4" @ "v4.32.1"

lean_lib PCPPR

@[default_target]
lean_exe pcppr where
  root := `Main
