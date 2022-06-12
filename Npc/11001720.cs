using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001720: Junta
/// </summary>
public class _11001720 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006971$
    // - You have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0728024507007019$
                // - Lava and ice... an unlikely, but breathtaking, view. It reminds me of you, $npcName:11001711[gender:1]$, and myself.
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
