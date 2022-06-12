using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000670: Misplaced Book
/// </summary>
public class _11000670 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20;30
    }

    // Select 0:
    // $script:0831180407002728$
    // - <font color="#909090">(One of these books seems out of place.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002729$
                // - No, no! I don't want to go back in there!
                return -1;
            case (20, 0):
                // $script:0831180407002730$
                // - Hey! Did you just throw me on the ground? 
                switch (selection) {
                    // $script:0831180407002731$
                    // - How did you end up on the bookshelf?
                    case 0:
                        // TODO: goto 21
                        // TODO: gotoFail 22
                        return -1;
                }
                return -1;
            case (21, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180407002732$
                // - A stupid monster brought me back here. Please, you've got to take me with you!
                return -1;
            case (22, 0):
                // $script:0831180407002733$
                // - Your bag is full! Make some room for me, will ya?
                return -1;
            case (30, 0):
                // $script:0831180407002734$
                // - <font color="#909090">(You always remember to put books back where you found them... right?)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
