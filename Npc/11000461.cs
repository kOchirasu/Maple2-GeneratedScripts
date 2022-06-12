using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000461: Isabel
/// </summary>
public class _11000461 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407002048$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002051$
                // - Others say Chief Hairdresser $npcName:11000255[gender:1]$ is the best, but I like $npcName:11000253[gender:0]$'s style.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
