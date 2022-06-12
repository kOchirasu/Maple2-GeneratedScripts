using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004224: Richelle
/// </summary>
public class _11004224 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806222707010796$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806222707010797$
                // - Hey, thanks for listening! We're Riot at the Danceclub. We all met during an audition and decided to form a band, kindred spirits and all that. We picked stage names to riff off the band name.
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
