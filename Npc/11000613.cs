using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000613: Louie
/// </summary>
public class _11000613 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002508$
    // - Huh?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002510$
                // - No one knows what it's like to toil in this place. Only another captive could understand. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
