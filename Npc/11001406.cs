using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001406: Gree
/// </summary>
public class _11001406 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217205907005403$
    // - You've got guts, walking around a place like this.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1222203907005471$
                // - Go away! We're on a mission!!
                switch (selection) {
                    // $script:1222203907005472$
                    // - You're awfully excited for someone on a mission.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1222203907005473$
                // - We aren't playing, if that's what you're trying to say! We don't get to play all day like you! We're on a very, very important <i>training</i> mission!!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
