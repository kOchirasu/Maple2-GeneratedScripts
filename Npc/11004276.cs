using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004276: Karkar Snake Statue
/// </summary>
public class _11004276 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011271$
    // - <font color="#909090">(Snake statues like this one can be found all over Karkar.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011272$
                // - <font color="#909090">(Snake statues like this one can be found all over Karkar.)</font>
                return 10;
            case (10, 1):
                // $script:0911203207011273$
                // - <font color="#909090">(You've noticed that these seem to be placed wherever poisonous snakes can be found. Perhaps they're a warning for the locals?)</font>
                return 10;
            case (10, 2):
                // $script:0911203207011274$
                // - <font color="#909090">(Then again, these statues look pretty old. Wouldn't the snake habitats have moved over time? Better be careful, just in case.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
