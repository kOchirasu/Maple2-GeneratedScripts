using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000143: Boen
/// </summary>
public class _11000143 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000581$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000584$
                // - Sigh... See that big hotel on the cliff? It dropped from the sky one day, literally out of the blue. Since then, monsters have been swarming the area. It's getting impossible to do anything.
                return -1;
            case (40, 0):
                // $script:0831180407000585$
                // - Huh? You think my name is funny. I disagree. 
                return 40;
            case (40, 1):
                // $script:0831180407000586$
                // - Boen is easy to remember and rolls off the tongue beautifully. Go to the top of that cliff and shout my name. It'll echo for a long time.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
