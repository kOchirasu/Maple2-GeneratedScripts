using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001109: Viata
/// </summary>
public class _11001109 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0908154107003727$
    // - Hey! Good to see you again!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0908154107003730$
                // - Mm? You're the one who saved me from $map:03009023$, aren't you?
                switch (selection) {
                    // $script:0907172207003699$
                    // - Why are you still in the Land of Darkness?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0908154107003731$
                // - That's... I want to stay with $npcName:11000614[gender:0]$. I never want to be separated from him again. 
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
