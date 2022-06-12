using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004148: Marina
/// </summary>
public class _11004148 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010567$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010568$
                // - Ever since we were little, it's always been me, $npcName:11004149$ and the sea, hehe!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
