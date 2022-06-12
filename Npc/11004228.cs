using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004228: Dortov
/// </summary>
public class _11004228 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806222707010807$
    // - Hmm...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806222707010808$
                // - I despise the noise and brutishness that permeates society. On this topic, it seems that I and this vision of elegance are of one mind.
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
