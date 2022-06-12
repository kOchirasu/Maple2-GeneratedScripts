using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000111: John
/// </summary>
public class _11000111 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407000456$
    // - What's up?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000457$
                // - Aww, I really don't think I can enter $map:02000116$.
                switch (selection) {
                    // $script:0831180407000458$
                    // - Why?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0831180407000459$
                // - A while back, I followed my uncle who works as a royal porter to the entrance of the forest. I couldn't see more than a few feet in front of me, the underbrush was so thick. Plus it was raining... I never want to go through that again. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
