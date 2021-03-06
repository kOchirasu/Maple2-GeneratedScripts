using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001312: Teddy
/// </summary>
public class _11001312 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1215203907005031$
    // - Glory to the empress!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1227194507005669$
                // - No matter how long these missions get, the guard is impervious to fatigue!
                //   <font color="#909090">(There are deep bags under his eyes.)</font> 
                return 30;
            case (30, 1):
                // $script:1227194507005670$
                // - Okay, I admit, I'm a <i>tiny</i> bit tired. I just haven't gotten used to my new quarters. I miss... Well, I have my reasons for being tired, okay? 
                switch (selection) {
                    // $script:1227194507005671$
                    // - Such as...?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1227194507005672$
                // - Please don't ask. I... I don't want to get into it.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
