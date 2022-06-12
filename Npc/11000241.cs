using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000241: Sally
/// </summary>
public class _11000241 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001019$
    // - Welcome.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001021$
                // - Are you heading to $map:02000135$? It's famous for its beautiful scenery. At the very top you'll find the Cloud Cafe, famous among young couples. You can take the cable car all the way up to the top if you want to see it.
                return 20;
            case (20, 1):
                // $script:0831180407001022$
                // - Our cable cars are made to last. They won't break, no matter how hard you jump! Please note that we won't be liable for injuries if you jump yourself right out of the car.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
