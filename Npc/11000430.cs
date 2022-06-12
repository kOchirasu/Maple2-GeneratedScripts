using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000430: Antoine
/// </summary>
public class _11000430 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;41
    }

    // Select 0:
    // $script:0831180407001791$
    // - I'm so glad I decided to come to the beach.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001793$
                // - $map:02000111$ is such a beautiful place to be! Except for the turtles. They're awful.
                return -1;
            case (40, 0):
                // $script:0831180407001794$
                // - Mm?
                switch (selection) {
                    // $script:0831180407001795$
                    // - $npcName:11000362[gender:0]$'s special...
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407001796$
                // - Not interested.
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
