using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000023: Toomy
/// </summary>
public class _11000023 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407000125$
    // - What's up?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000126$
                // - Are you also trying to attend the court? I was on my way there... stopping to sample some delicious food along the way, of course... and had my plans dashed by this wretched rift! I suppose I could try the forest, but it's fairly frightening.
                switch (selection) {
                    // $script:0831180407000127$
                    // - Wait, can you get around the rift through the forest?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0831180407000128$
                // - That's what I heard! Follow the path between the trees over there to $map:02000116$, and then keep on until you get to $map:02000001$.
                return 11;
            case (11, 1):
                // $script:0831180407000129$
                // - I wouldn't try it if I were you, though. A few folks have faced the forest... but none have returned from $map:02000116$.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
