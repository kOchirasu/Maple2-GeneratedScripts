using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003964: Striker
/// </summary>
public class _11003964 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614143707010019$
    // - You seem like you're pretty tough too.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614143707010020$
                // - You ever heard of the Gray Wolf? Well you're looking at him! The man, the myth, the legend! What do you mean you've never heard of me...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
