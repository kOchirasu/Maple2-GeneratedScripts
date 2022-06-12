using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000693: Ruru
/// </summary>
public class _11000693 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002796$
    // - $MyPCName$, welcome.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002799$
                // - $npcName:11000032[gender:0]$ is the only one who stayed with me when everyone else turned their backs.
                return 30;
            case (30, 1):
                // $script:0831180407002800$
                // - So I'm going to stand by him, no matter what happens.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
