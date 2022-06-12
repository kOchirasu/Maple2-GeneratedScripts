using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003517: Ashim
/// </summary>
public class _11003517 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0817044507008848$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0817044507008851$
                // - What?
                switch (selection) {
                    // $script:0817044507008852$
                    // - Tell me about the five auras.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0817044507008853$
                // - Aur-what? Look, I just want to finish my exam and grab some grub.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
