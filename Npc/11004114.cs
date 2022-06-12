using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004114: Tinchai
/// </summary>
public class _11004114 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010471$
    // - Hmm... Did you need something?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010472$
                // - Sounds like you've got an important mission! I'm sure you'll succeed!
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
