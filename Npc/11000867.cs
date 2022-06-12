using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000867: Prussell
/// </summary>
public class _11000867 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407003133$
    // - Feel free to take a look around.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407003137$
                // - Bugs love delicious fruit. Just look at all these flies in my shop! That should tell you how sweet my fruit is.
                return 40;
            case (40, 1):
                // $script:0831180407003138$
                // - My prices are lower than any supermarket's. Here, come try some samples.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
