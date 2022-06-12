using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004357: Evelyn
/// </summary>
public class _11004357 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011767$
    // - What a relief.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011768$
                // - Thank you very much for helping us, $MyPCName$.
                return 10;
            case (10, 1):
                // $script:1120173007011847$
                // - And... forgive $npcName:11004349[gender:0]$. I was the one who messed up, venting my anger in my diary...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
