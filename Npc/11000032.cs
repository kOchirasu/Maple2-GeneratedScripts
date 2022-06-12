using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000032: Einos
/// </summary>
public class _11000032 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000183$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000184$
                // - We should let $npcName:11000031[gender:0]$ know his identity and ask for advice. Meet me in $map:02000035$.
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
