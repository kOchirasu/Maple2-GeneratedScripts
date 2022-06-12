using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000150: Justin
/// </summary>
public class _11000150 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000640$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000643$
                // - People spend their days scrambling around, trying to have it all. That's no way to live. Just enjoy the moment.
                return -1;
            case (40, 0):
                // $script:0321130807008115$
                // - Unless this is extremely important, I'm in no mood to chat.
                switch (selection) {
                    // $script:0321130807008116$
                    // - Did you see a guard get dragged away?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0321130807008117$
                // - Now that you mention it, there was an especially pitiful-looking soldier... He was dragged off in the direction of $map:52000119$, to the northeast.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
