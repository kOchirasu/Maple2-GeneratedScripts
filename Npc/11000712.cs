using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000712: Tortie
/// </summary>
public class _11000712 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002868$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002871$
                // - Dad doesn't want to play with me. $MyPCName$, could you play with me?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
