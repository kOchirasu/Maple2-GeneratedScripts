using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001054: Nomar
/// </summary>
public class _11001054 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003600$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003603$
                // - People say that sometimes dreams, do come true. I hope they're right.
                switch (selection) {
                    // $script:0831180407003604$
                    // - What's your dream?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407003605$
                // - My dream isn't much. I just want to be a successful businessman. I may be delivering pizzas now, but I know I can make it big if I work hard enough.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
