using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001309: Devin
/// </summary>
public class _11001309 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1215203907005028$
    // - Ugh, my head...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1227194507005659$
                // - I've got more cases on my plate than I could ever solve in a single lifetime.
                return 40;
            case (40, 1):
                // $script:1227194507005660$
                // - Sure, I'm happy that $map:02010002$ is growing. But does the crime have to grow with it? Our prison is bursting at the seams!
                return 40;
            case (40, 2):
                // $script:1227194507005661$
                // - This isn't police work. It's war! But somebody's got to protect the city, right?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
