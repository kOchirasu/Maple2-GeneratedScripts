using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001702: Tinchai
/// </summary>
public class _11001702 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0719003107006786$
    // - $MyPCName$, are you all right?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006911$
                // - If $npcName:11001557[gender:0]$ had gotten here a minute later...
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
