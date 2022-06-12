using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003243: Tinnie
/// </summary>
public class _11003243 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008145$
    // - What's wrong?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008146$
                // - I understand what $npcName:11003240[gender:0]$ is going through, but it's past time for him to grow up.
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
