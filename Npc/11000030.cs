using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000030: Robin
/// </summary>
public class _11000030 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000178$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000180$
                // - Bullies are the worst. How can anyone pick on someone weaker than themselves?
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
