using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004255: Mouse
/// </summary>
public class _11004255 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0829171107010970$
    // - Just look at that delicious candy and that sweet cream! How could anyone possibly resist? Hehe.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0829171107010971$
                // - Just look at that delicious candy and that sweet cream! How could anyone possibly resist? Hehe.
                return 10;
            case (10, 1):
                // $script:0831140807011013$
                // - So sweet! So very, very sweet. We're so blessed to eat such tastiness. Wouldn't you like to be blessed, too?
                switch (selection) {
                    // $script:0831140807011014$
                    // - Aren't you worried about getting fat?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0831140807011015$
                // - Oh, no. Oh, no, no, no, never. Doesn't it just look irresistibly scrumptious? Don't you want to just take a lick?
                switch (selection) {
                    // $script:0831140807011016$
                    // - It can't be that great...
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0831140807011017$
                // - You see those monsters over there? They're a long way from their natural habitat. They're all here because they're in love with these sweets. Such tasty, tasty treats.
                switch (selection) {
                    // $script:0831140807011018$
                    // - That actually sounds kind of dangerous.
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0831140807011019$
                // - Dangerous? No way! Would we lie to you? There's nothing sweeter than to live life here amongst the world's tastiest treats.
                switch (selection) {
                    // $script:0831140807011020$
                    // - Uh, yeah. This is where I get the heck out of here.
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:0831140807011021$
                // - Where are you going? Have a taste!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
